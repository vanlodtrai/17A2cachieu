import csv
import random
def create_deck():
    """Tạo một bộ bài với 5 cặp lá bài giống nhau."""
    cards = list(range(1, 6)) * 2  # Tạo 5 cặp lá bài giống nhau
    random.shuffle(cards)  # Trộn ngẫu nhiên các lá bài
    return cards
def flip_card(deck, flipped_positions):
    """Người chơi lật một lá bài."""
    while True:
        try:
            position = int(input("Nhập vị trí lá bài bạn muốn lật (0-9): "))
            if position not in range(10):
                raise ValueError("Vị trí không hợp lệ. Vui lòng nhập số từ 0 đến 9.")
            if position in flipped_positions:
                raise ValueError("Lá bài đã được lật. Vui lòng chọn vị trí khác.")
            break
        except ValueError as e:
            print(e)
    flipped_positions.add(position)
    return position
def check_match(deck, pos1, pos2):
    """Kiểm tra xem hai lá bài có giống nhau không."""
    return deck[pos1] == deck[pos2]
def calculate_probability(probabilities):
    prob_pair = 0
    for card, prob in probabilities.items():
        prob_pair += prob * prob
    return prob_pair
def save_results_to_csv(results, filename):
    with open("D:Github/27134600091_Nguyen_Huu_Van_17A2_Ca-sang/Nguyễn Hữu Văn_23174600091/ket_qua.csv", mode='w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Vị trí lá bài", "Mã lá bài", "Xác suất xuất hiện", "Tìm được cặp (True/False)"])
        for result in results:
            writer.writerow(result)
    print(f"Kết quả đã được lưu vào file CSV tại {filename}")
def main():
    deck = create_deck()
    flipped_positions = set()
    score = 0
    attempts = 0
    results = []
    probabilities = {i: 0.1 for i in range(1, 6)}  # Tạo xác suất giả định cho các lá bài
    while len(flipped_positions) < len(deck):
        pos1 = flip_card(deck, flipped_positions)
        pos2 = flip_card(deck, flipped_positions) 
        match = check_match(deck, pos1, pos2)
        if match:
            score += 1
            print(f"Tìm được cặp tại vị trí {pos1} và {pos2}.")
        else:
            flipped_positions.remove(pos1)
            flipped_positions.remove(pos2)
            print(f"Lá bài tại vị trí {pos1} và {pos2} không giống nhau.") 
        attempts += 1
        results.append([pos1, deck[pos1], probabilities[deck[pos1]], match])
        results.append([pos2, deck[pos2], probabilities[deck[pos2]], match])
    probability_of_pair = calculate_probability(probabilities)
    print(f"Số điểm đạt được: {score}")
    print(f"Số lần thử: {attempts}")
    print(f"Xác suất tìm được cặp lá bài giống nhau: {probability_of_pair:.2f}")
    save_results_to_csv(results, "ket_qua.csv")
if __name__ == "__main__":
    main()
