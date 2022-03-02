class Voting:
    def __init__(self):
        self.ga3 = [0, 0, 0, 0, 0]
        self.ga4 = [0, 0, 0, 0, 0]
        self.hrc = [0, 0, 0, 0, 0]
        self.sc = [0, 0, 0, 0, 0]
        self.ecosoc = [0, 0, 0, 0, 0]
        self.who = [0, 0, 0, 0, 0]
        self.users = []


    def check_voter(self, member):
        if len(self.users) == 0:
            self.users.append(member)
            return True
        else:
            for i in self.users:
                if member == i:
                    return False
                else:
                    self.users.append(member)
                    return True

    def vote(self, vote, comm):
        if vote == "f":
            data = self.__getattribute__(comm)
            data[0] += 1
            self.__setattr__(comm, data)
        elif vote == "ag":
            data = self.__getattribute__(comm)
            data[1] += 1
            self.__setattr__(comm, data)
        elif vote == "ab":
            data = self.__getattribute__(comm)
            data[2] += 1
            self.__setattr__(comm, data)
        elif vote == "p":
            data = self.__getattribute__(comm)
            data[3] += 1
            self.__setattr__(comm, data)
        elif vote == "pv":
            data = self.__getattribute__(comm)
            data[4] += 1
            self.__setattr__(comm, data)

    def end_vote(self, proc, comm):
        if proc == "fa":
            f = self.__getattribute__(comm)[0]
            ag = self.__getattribute__(comm)[1]
            ab = self.__getattribute__(comm)[2]
            self.clear(comm)
            return f"For: {f}. Against: {ag} Abstain: {ab}."
        elif proc == "pv":
            p = self.__getattribute__(comm)[3]
            v = self.__getattribute__(comm)[4]
            print(v)
            self.clear(comm)
            return f"Present: {p}.          Present and Voting: {v}."


    def clear(self, comm):
        data = self.__getattribute__(comm)
        data[0] = 0
        data[1] = 0
        data[2] = 0
        data[3] = 0
        data[4] = 0
        self.users.clear()



