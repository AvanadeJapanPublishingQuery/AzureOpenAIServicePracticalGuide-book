import semantic_kernel as sk
import random
from semantic_kernel.skill_definition import sk_function

# Azure OpenAI API Keyの設定
api_key = "YOUR AZURE OPENAI API KEY"
endpoint = "YOUR AZURE OPENAI ENDPOINT"
deployment = "gpt-35-turbo-16k"

kernel = sk.Kernel()

class GenerateNumberSkill:
    """
    Description: 1からxの間の数を生成する.
    """

    @sk_function(
        description="Generate a random number between 1-x",
        name="GenerateNumberThreeOrHigher"
    )
    def generate_number_three_or_higher(self, input: str) -> str:
        """
        1から<input>の数を生成する
        Example:
            "8" => rand(1,8)
        Args:
            input -- The upper limit for the random number generation
        Returns:
            int value
        """
        try:
            return str(random.randint(1, int(input))) 
        except ValueError as e:
            print(f"Invalid input {input}")
            raise e

generate_number_skill = kernel.import_skill(GenerateNumberSkill())

# 関数の実行
generate_number_three_or_higher = generate_number_skill["GenerateNumberThreeOrHigher"]
number_result = generate_number_three_or_higher(6)
print(number_result)