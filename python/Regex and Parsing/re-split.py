regex_pattern = r"[\W]"

import re

print("\n".join(re.split(regex_pattern, input())))
