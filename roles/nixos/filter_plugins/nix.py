#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'nix_array': self.filter_array
        }

    def filter_array(self, array):
        nix_array_string = '[' + array + ']'
        return nix_array_string