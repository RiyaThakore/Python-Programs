def toLowerCase(self, s):
        return "".join(chr(ord(i) + 32) if "A" <= i <= "Z" else i for i in s)
