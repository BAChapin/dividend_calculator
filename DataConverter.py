# ****************************** Developer Notes ******************************
#
# *****************************************************************************

class DataConverter:

    def bool_input(output: str) -> bool:
        """A custom input method specifically to collect booleans from the user"""
        userInput = input(output)

        return DataConverter.str_to_bool(userInput)

    def str_to_bool(check: str) -> bool:
        """A method to convert user input string to a boolean"""

        trueOptions = ["true", "yes", "t", "y"]

        if check.lower() in trueOptions:
            return True
        else:
            return False

    def create_header(title: str,
                      wildcard: str,
                      length: int,
                      withSpace: bool = True) -> str:
        isTitleOdd = True if (len(title) % 2) > 0 else False
        wildcardSize = length - len(title)

        if withSpace and not isTitleOdd:
            wildcardSize -= 2

        wildcardLength = int(wildcardSize / 2)
        headerLeft = wildcard * (wildcardLength if not isTitleOdd else wildcardLength - 1)
        newTitle = title if not withSpace else " {} ".format(title)
        headerRight = wildcard * wildcardLength

        return "{0}{1}{2}".format(headerLeft, newTitle, headerRight)
