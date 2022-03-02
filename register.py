class Register:
    def __init__(self):
        self.role_dict = {}
        self.users = []
        self.countries_1 = ['🇦🇫', '🇦🇱', '🇦🇺', '🇧🇷', '🇨🇦', '🇨🇳', '🇪🇨', '🇫🇷', '🇬🇦', '🇩🇪', '🇬🇭', '🇮🇳', '🇮🇩', '🇮🇪']
        self.countries_2 = ['🇰🇪', '🇲🇽', '🇳🇴', '🇵🇸', '🇷🇺', '🇬🇧', '🇦🇪', '🇺🇸', '🇵🇱', '🇲🇱', '🇹🇩', '🇳🇱', '🇲🇦']
        self.countries_sc = ["🇦🇱", "🇧🇷", "🇨🇳", "🇫🇷", "🇬🇦", "🇬🇭", "🇮🇳", "🇮🇪", "🇰🇪", "🇲🇽", "🇳🇴", "🇷🇺", "🇬🇧", "🇦🇪", "🇺🇸", "🇧🇪", "🇬🇾"]
        self.committees = ['delegate', 'P5', 'SC', 'GA3', 'ECOSOC', 'HRC', 'GA4', 'WHO']

    def check_user(self, member):
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

    def create_reg(self, message):
        reg_list = str(message).replace("!register ", "").split(", ")
        return reg_list

    def check_reg(self, reg_list):
            if reg_list[0] in self.committees and len(reg_list) == 3:
                return True
            else:
                return False

    def find_roles(self, reg_list):
        comm = reg_list[0]
        roles = [self.role_dict.get(comm), self.role_dict.get("delegate")]
        return roles

    def setup_nick(self, reg_list):
        new_nick = f"{reg_list[0]}, {reg_list[1]} | {reg_list[2]}"
        return new_nick

    def setup_dict(self):
        with open("final_server_roles.txt", "r") as f:
            for line in f:
                (key, value) = line.split()
                self.role_dict[key] = int(value)

    def placard_channels(self):
        chan_dict = []
        with open("final_server_chans.txt", "r") as f:
            for line in f:
                (key, value) = line.split()
                chan_dict.append(value)
        return chan_dict

