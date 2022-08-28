# 05 Replace space in string

## Question
> Write a function to replace space in a string with '%20'. For example, if input is 'We are happy.', the output should be 'We%20are%20happy.'.

### Solution
If the scan starts from the beginning of the string with length of <em>n</em>, for each space, we need to move the following <em>O</em>(<em>n</em>) characters. For a string with <em>n</em> spaces, the total time complexity is <em>O</em>(<em>n</em><sup>2</sup>).

Therefore we start the scan from the end of the string and create 2 pointers, one pointing to the end of the original string and one pointing to the end of the new string. The length of the new string is calculated by counting the number of spaces in the original string first. In this way, we only need to go through the string once so the time complexity is <em>O</em>(<em>n</em>).
```python
def replace_space(string: str) -> str:
    if len(string) == 0:
        raise ValueError('String is empty.')

    length_space = 0
    for s in string:
        if s == ' ':
            length_space += 1

    length_new = len(string) + length_space*2
    new_string = [' '] * length_new
    index_original = len(string) - 1
    index_new = length_new - 1
    while index_new >= index_original and index_original >= 0:
        if string[index_original] == ' ':
            new_string[index_new-2:index_new+1] = ['%', '2', '0']
            index_new -= 3
            index_original -= 1
        else:
            new_string[index_new] = string[index_original]
            index_original -= 1
            index_new -= 1
    return ''.join(new_string)
    ```
