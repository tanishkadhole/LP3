class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


def print_job_sequence(jobs):
    # Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = len(jobs)
    # Find the maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Initialize result array and slot array
    result = ['X'] * max_deadline
    slot = [False] * max_deadline

    # Iterate through all jobs
    for job in jobs:
        # Find a free slot for this job (we start from the last possible slot)
        for j in range(min(max_deadline - 1, job.deadline - 1), -1, -1):
            if not slot[j]:
                result[j] = job.id
                slot[j] = True
                break

    # Print the result
    print("Job Sequence:", ' '.join(job for job in result if job != 'X'))

    # Calculate and print the total profit
    total_profit = sum(job.profit for job in jobs if job.id in result)
    print("Total Profit:", total_profit)


if __name__ == "__main__":
    jobs = [
        Job('a', 2, 100),
        Job('b', 1, 19),
        Job('c', 2, 27),
        Job('d', 1, 25),
        Job('e', 3, 15)
    ]

    print("Job Sequencing with Deadlines:")
    print_job_sequence(jobs)

    """
    # Input from the user :
    num_jobs = int(input("Enter the number of jobs: "))
    jobs = []

    for _ in range(num_jobs):
        job_id = input("Enter job ID (single character): ")
        deadline = int(input(f"Enter deadline for job {job_id}: "))
        profit = int(input(f"Enter profit for job {job_id}: "))
        jobs.append(Job(job_id, deadline, profit))

    print("\nJob Sequencing with Deadlines:")
    print_job_sequence(jobs)
    """
