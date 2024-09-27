#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'nix_list': self.filter_list
        }

    def filter_list(self, list):
        nix_array_string = '[' + " ".join(array) + '];'
        return nix_array_string