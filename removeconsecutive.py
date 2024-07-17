def remove_consecutive_duplicates(s: str) -> str:
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            while stack and stack[-1] == char:
                stack.pop()
        else:
            stack.append(char)
    
    return ''.join(stack)

# Example usage
input_str = "baaab"
output_str = remove_consecutive_duplicates(input_str)
print(output_str)