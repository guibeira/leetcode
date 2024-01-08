# @leet start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  # Criar um dicionário para armazenar os números e seus índices

        for i, num in enumerate(nums):
            complement = (
                target - num
            )  # Calcular o complemento necessário para atingir a soma desejada

            # Verificar se o complemento já está no dicionário (ou seja, encontramos um par)
            if complement in num_dict:
                return [num_dict[complement], i]  # Retornar os índices dos dois números

            # Caso contrário, armazenar o número atual no dicionário com seu índice
            num_dict[num] = i

        return None


# @leet end
