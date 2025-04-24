import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

START_DATE = datetime(2020, 8, 1)
now = datetime.now()
experience = relativedelta(now, START_DATE)

readme_path = "/home/runner/work/charan-vendra/charan-vendra/README.md"

with open(readme_path, "r", encoding="utf-8") as file:
    content = file.read()

experience_pattern = re.compile(r"_\d+ years_ ~ _\d+ months_ ~ _\d+ days_")
new_experience = f"_{experience.years} years_ ~ _{experience.months} months_ ~ _{experience.days} days_"

copyright_pattern = re.compile(r"© \d+")
new_copyright = f"© {now.year}"

content = experience_pattern.sub(new_experience, content)
content = copyright_pattern.sub(new_copyright, content)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
