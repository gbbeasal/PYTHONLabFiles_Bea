#sa os.getenv() no need to specify a variable before you run the code eh kase you can set a default value
#o os.getenv(variable_name, default-variable_value)

import os
stage = os.getenv("STAGE", "dev").upper()
output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output
print(output)


'''
####export STAGE='staging'
OLD:
import os
stage = os.environ["STAGE"].upper()
output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)
'''