class Solution:
    def sortSentence(self, s: str) -> str:
        sentences = s.split(" ")
        sorted_sentence = [""] * (len(sentences))
        for a_word in sentences:
            order = int(a_word[-1])
            sorted_sentence[order-1] = a_word[:-1]
        return " ".join(sorted_sentence)