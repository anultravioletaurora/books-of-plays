#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'nix_list': self.filter_list
        }

    def filter_list(self, list: list):
        nix_list_string = '[' + " ".join(list) + '];'

        # list will have str and dict in it
        return nix_list_string