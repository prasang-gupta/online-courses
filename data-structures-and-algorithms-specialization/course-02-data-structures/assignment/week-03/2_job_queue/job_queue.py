# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at", "finishtime"])

class Heap:

    def __init__(self, arrdata):
        self.data = arrdata
        size = len(arrdata)
        depth = 2
        while (size // depth) != 0:
            depth = depth * 2
        start = int((depth/2) - 2)

        for i in range(start, -1, -1):
            self.siftdown(i)

    def siftdown(self, idx):
        size = len(self.data)
        idxc1 = (2 * idx) + 1
        idxc2 = (2 * idx) + 2

        if idxc1 < size and idxc2 < size:
            if self.data[idxc1].finishtime != self.data[idxc2].finishtime:
                if self.data[idxc1].finishtime < self.data[idxc2].finishtime:
                    minval = self.data[idxc1].finishtime
                    minidx = idxc1
                else:
                    minval = self.data[idxc2].finishtime
                    minidx = idxc2
            else:
                if self.data[idxc1].worker < self.data[idxc2].worker:
                    minval = self.data[idxc1].finishtime
                    minidx = idxc1
                else:
                    minval = self.data[idxc2].finishtime
                    minidx = idxc2
        else:
            if idxc1 < size:
                minval = self.data[idxc1].finishtime
                minidx = idxc1
            elif idxc2 < size:
                minval = self.data[idxc2].finishtime
                minidx = idxc2
            else:
                return 0

        if minval < self.data[idx].finishtime:
            temp = self.data[minidx]
            self.data[minidx] = self.data[idx]
            self.data[idx] = temp
            self.siftdown(minidx)
        elif minval == self.data[idx].finishtime:
            if self.data[minidx].worker < self.data[idx].worker:
                temp = self.data[minidx]
                self.data[minidx] = self.data[idx]
                self.data[idx] = temp
                self.siftdown(minidx)

    def change_priority(self, newjob):
        newjob_obj = AssignedJob(self.data[0].worker, self.data[0].finishtime, self.data[0].finishtime + newjob)
        self.data[0] = newjob_obj
        self.siftdown(0)
        return newjob_obj

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    data = [0] * n_workers
    for i in range(n_workers):
        if i >= len(jobs):
            return result
        data[i] = AssignedJob(i, 0, jobs[i])
        result.append(data[i])
    
    if n_workers == len(jobs):
        return result
    
    heap = Heap(data)

    for i in range(n_workers, len(jobs)):
        result.append(heap.change_priority(jobs[i]))
    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    # n_workers, n_jobs = 4, 20
    # jobs = [1 for _ in range(20)]
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
