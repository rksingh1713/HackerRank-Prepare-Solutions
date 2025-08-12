regex_pattern = r"M{,3}(D?C{,3}|C[DM])(L?X{,3}|X[LC])(V?I{,3}|I[VX])$"

import re

print(str(bool(re.match(regex_pattern, input()))))
