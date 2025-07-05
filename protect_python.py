def secret_function():
    secret_value = 42
    print("🔐 This is a protected function. Secret =", secret_value)

def another_function():
    print("✅ This is a public part of the app.")

if __name__ == "__main__":
    another_function()
    secret_function()
