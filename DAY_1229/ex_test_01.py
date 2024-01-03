# --------------------------------------------
# [실습1] 단어를 입력 받은 후 아래 코드를 작성하세요.
# - 입력 받은 단어가 알파벳만으로 구성되어 있는지 검사
# - 입력 받은 단어가 숫자만으로 구성되어 있는지 검사
# - 입력 받은 단어가 모두 대문자만으로 구성되어 있는지 검사
# - 입력 받은 단어가 모두 소문자만으로 구성되어 있는지 검사
# ---------------------------------------------
word = input('Enter a word :')
wc = print(f'Is {word} only character? => {word.isalpha()}')
wd = print(f'Is {word} only number? => {word.isnumeric()}')
wu = print(f'Is {word} only uppercase? => {word.isupper()}')
wl = print(f'Is {word} only lowercase? => {word.islower()}')


# ---------------------------------------------
# [실습2] 파일명을 입력 받은 후 아래 코드를 작성하세요. => str 전용 함수인 메서드 활용
# - 입력 받은 파일이 text 파일인지 검사
# - 입력 받은 파일이 jpg 파일인지 검사
# - 입력 받은 파일이 py 파일인지 검사
# ---------------------------------------------
file = input("Input a file name : ")
ft = print(f'text file? => {file.endswith("txt")}')
fj = print(f'jpg file? => {file.endswith("jpg")}')
fp = print(f'py file? => {file.endswith("py")}')