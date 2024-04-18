for i in range(16,46):
    text = """
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="refresh" content="0; url=https://www.youtube.com/watch?v=xvFZjo5PgG0" />
    </head>
</html>
"""
    with open(f'./EX{i}.html','w') as f:
        f.write(text)
        f.close()