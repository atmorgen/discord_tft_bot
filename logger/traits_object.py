class TraitsObject:

    def __init__(self):
        self.trait_list = {}
        self.response_object = None

    def process_traits(self, traits):
        for trait in traits:
            if trait['name'] in self.trait_list:
                self.trait_list[trait['name']] += trait['tier_current']
            else:
                self.trait_list[trait['name']] = trait['tier_current']

    def set_averages(self, total_count):
        for key in self.trait_list:
            self.trait_list[key] = self.trait_list[key]/total_count

    def to_string(self):
        trait_list_final = {k: v for k, v in sorted(self.trait_list.items(), key=lambda item: item[1], reverse=True)}
        response = "\nTrait Tier Averages:"
        for k, v in trait_list_final.items():
            if v >= 0.3:
                response += f'\n        `{round(v, 1)}` <---- `{k.replace("Set4_","")}`'

        return response