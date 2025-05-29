import random
import time
import os

def modify_text(text, entropy_level):
    # Convert entropy level to a probability (0-1)
    prob = entropy_level / 100
    
    # Mapping dictionaries for small caps, superscript, and subscript
    small_caps = {
        'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ғ', 'g': 'ɢ', 'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ', 's': 's', 't': 'ᴛ', 'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 'y': 'ʏ', 'z': 'ᴢ',
        'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ғ', 'G': 'ɢ', 'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ', 'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ', 'O': 'ᴏ', 'P': 'ᴘ', 'Q': 'ǫ', 'R': 'ʀ', 'S': 's', 'T': 'ᴛ', 'U': 'ᴜ', 'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 'Y': 'ʏ', 'Z': 'ᴢ',
    }
    superscript = {
        'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ', 'f': 'ᶠ', 'g': 'ᵍ', 'h': 'ʰ', 'i': 'ᶦ', 'j': 'ʲ', 'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'n': 'ⁿ', 'o': 'ᵒ', 'p': 'ᵖ', 'q': 'ᵠ', 'r': 'ʳ', 's': 'ˢ', 't': 'ᵗ', 'u': 'ᵘ', 'v': 'ᵛ', 'w': 'ʷ', 'x': 'ˣ', 'y': 'ʸ', 'z': 'ᶻ',
        'A': 'ᵃ', 'B': 'ᵇ', 'C': 'ᶜ', 'D': 'ᵈ', 'E': 'ᵉ', 'F': 'ᶠ', 'G': 'ᵍ', 'H': 'ʰ', 'I': 'ᶦ', 'J': 'ʲ', 'K': 'ᵏ', 'L': 'ˡ', 'M': 'ᵐ', 'N': 'ⁿ', 'O': 'ᵒ', 'P': 'ᵖ', 'Q': 'ᵠ', 'R': 'ʳ', 'S': 'ˢ', 'T': 'ᵗ', 'U': 'ᵘ', 'V': 'ᵛ', 'W': 'ʷ', 'X': 'ˣ', 'Y': 'ʸ', 'Z': 'ᶻ',
    }
    subscript = {
        'a': 'ₐ', 'b': 'ᵦ', 'c': '𝒸', 'd': '𝒹', 'e': 'ₑ', 'f': '𝒻', 'g': '𝓰', 'h': 'ₕ', 'i': 'ᵢ', 'j': 'ⱼ', 'k': 'ₖ', 'l': 'ₗ', 'm': 'ₘ', 'n': 'ₙ', 'o': 'ₒ', 'p': 'ₚ', 'q': 'ᵩ', 'r': 'ᵣ', 's': 'ₛ', 't': 'ₜ', 'u': 'ᵤ', 'v': 'ᵥ', 'w': '𝓌', 'x': 'ₓ', 'y': 'ᵧ', 'z': '𝓏',
        'A': 'ₐ', 'B': 'ᵦ', 'C': '𝒸', 'D': '𝒹', 'E': 'ₑ', 'F': '𝒻', 'G': '𝓰', 'H': 'ₕ', 'I': 'ᵢ', 'J': 'ⱼ', 'K': 'ₖ', 'L': 'ₗ', 'M': 'ₘ', 'N': 'ₙ', 'O': 'ₒ', 'P': 'ₚ', 'Q': 'ᵩ', 'R': 'ᵣ', 'S': 'ₛ', 'T': 'ₜ', 'U': 'ᵤ', 'V': 'ᵥ', 'W': '𝓌', 'X': 'ₓ', 'Y': 'ᵧ', 'Z': '𝓏',
    }
    # Zalgo script dictionary (lowercase only, as provided)
    zalgo = {
        'a': 'ǻ̷͚̭ͅ', 'b': 'b̶͈͓̘͛̈́̄', 'c': 'ć̴͓̭͓̿', 'd': 'ď̷͖̭͒͂', 'e': 'e̴͙̜͌̓͊', 'f': 'f̴͚͖̥̿͝͝', 'g': 'g̶̝͔̳̈́', 'h': 'ḫ̸̗̱̾̊', 'i': 'ḯ̸̲̩', 'j': 'j̸̫͇͋̅̆', 'k': 'ḱ̶͍̥̅', 'l': 'l̵͇̍́', 'm': 'm̵̤͔̊͝', 'n': 'n̷̜̥̲̑', 'o': 'ô̵͛͂ͅ', 'p': 'p̷͖̭̌͒͂', 'q': 'q̵̪̺̆̎̎', 'r': 'r̴͙̜͌̓͊', 's': 's̴͚͖̥̿͝͝', 't': 'ẗ̶̝͔̳́', 'u': 'u̸̮̗̱̾̊', 'v': 'v̸̲̩̈́', 'w': 'w̸̫͇͋̅̆', 'x': 'x̶͍̥́̅', 'y': 'y̵͇̍́', 'z': 'z̵̤͔̊͝',
        'A': 'ǻ̷͚̭ͅ', 'B': 'b̶͈͓̘͛̈́̄', 'C': 'ć̴͓̭͓̿', 'D': 'ď̷͖̭͒͂', 'E': 'e̴͙̜͌̓͊', 'F': 'f̴͚͖̥̿͝͝', 'G': 'g̶̝͔̳̈́', 'H': 'ḫ̸̗̱̾̊', 'I': 'ḯ̸̲̩', 'J': 'j̸̫͇͋̅̆', 'K': 'ḱ̶͍̥̅', 'L': 'l̵͇̍́', 'M': 'm̵̤͔̊͝', 'N': 'n̷̜̥̲̑', 'O': 'ô̵͛͂ͅ', 'P': 'p̷͖̭̌͒͂', 'Q': 'q̵̪̺̆̎̎', 'R': 'r̴͙̜͌̓͊', 'S': 's̴͚͖̥̿͝͝', 'T': 'ẗ̶̝͔̳́', 'U': 'u̸̮̗̱̾̊', 'V': 'v̸̲̩̈́', 'W': 'w̸̫͇͋̅̆', 'X': 'x̶͍̥́̅', 'Y': 'y̵͇̍́', 'Z': 'z̵̤͔̊͝',
    }
    
    # Convert text to list for character manipulation
    chars = list(text)
    
    # Randomly modify characters based on entropy
    for i in range(len(chars)):
        if random.random() < prob:
            # Randomly capitalize/uncapitalize
            chars[i] = chars[i].swapcase()
            # Small chance to convert to small caps, superscript, subscript, or zalgo
            style_chance = prob / 2  # Tune this for how often it happens
            if random.random() < style_chance:
                style = random.choice(['small_caps', 'superscript', 'subscript', 'zalgo'])
                if style == 'small_caps' and chars[i] in small_caps:
                    chars[i] = small_caps[chars[i]]
                elif style == 'superscript' and chars[i] in superscript:
                    chars[i] = superscript[chars[i]]
                elif style == 'subscript' and chars[i] in subscript:
                    chars[i] = subscript[chars[i]]
                elif style == 'zalgo' and chars[i] in zalgo:
                    chars[i] = zalgo[chars[i]]
            
    result = ''.join(chars)

    # Per-space entropy-based modification
    new_result = []
    i = 0
    while i < len(result):
        if result[i] == ' ':
            if random.random() < prob:  # Only affect a % of spaces based on entropy
                # Choose transformation, more extreme at higher entropy
                space_mod = random.choices(
                    ["double", "triple", "newline", "remove", "none"],
                    weights=[
                        max(0, 40 - entropy_level),  # double spaces more likely at low entropy
                        max(0, 30 - entropy_level // 2),  # triple spaces at mid entropy
                        entropy_level,  # newlines more likely at high entropy
                        entropy_level,  # remove more likely at high entropy
                        max(0, 100 - entropy_level)  # none more likely at low entropy
                    ],
                    k=1
                )[0]
                if space_mod == "double":
                    new_result.append('  ')
                elif space_mod == "triple":
                    new_result.append('   ')
                elif space_mod == "newline":
                    new_result.append('\n')
                elif space_mod == "remove":
                    pass  # don't add any space
                else:
                    new_result.append(' ')
            else:
                new_result.append(' ')
            i += 1
        else:
            new_result.append(result[i])
            i += 1
    result = ''.join(new_result)

    return result

def main():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'entropy_text.txt')
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
        entropy = 0
        increment = 100 / len(lines)  # Evenly distribute entropy increase
        
        for line in lines:
            line = line.strip()
            entropy = min(100, entropy + increment)  # Cap at 100%
            
            # Clear screen (works for both Windows and Unix)
            print('\033[2J\033[H', end='')
            
            # Display entropy percentage
            print(f"Current Entropy: {entropy:.1f}%\n")
            
            # Display modified text
            print(modify_text(line, entropy))
            
            # Pause between lines
            wait = input("Press Enter to continue...")
            
    except FileNotFoundError:
        print("Error: entropy_text.txt not found in the current directory")
        
if __name__ == "__main__":
    main()
