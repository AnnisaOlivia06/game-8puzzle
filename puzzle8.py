import random

def buat_puzzle():
    """Membuat puzzle 3x3 secara acak dengan angka 0 di sudut kanan bawah"""
    puzzle = list(range(9))
    random.shuffle(puzzle)

    # Pastikan angka 0 berada di indeks terakhir (posisi kanan bawah)
    puzzle.remove(0)
    puzzle.append(0)
    return puzzle

def tampilkan_puzzle(puzzle):
  """Menampilkan puzzle ke layar"""
  for i in range(3):
    print(' '.join(map(str, puzzle[i*3:i*3+3])))

def geser(puzzle, arah):
  """Menggeser angka kosong (0) sesuai arah"""
  kosong = puzzle.index(0)
  bar, kol = divmod(kosong, 3)

  if arah == 'w' and bar > 0:
    puzzle[kosong], puzzle[kosong-3] = puzzle[kosong-3], puzzle[kosong]
  elif arah == 's' and bar < 2:
    puzzle[kosong], puzzle[kosong+3] = puzzle[kosong+3], puzzle[kosong]
  elif arah == 'a' and kol > 0:
    puzzle[kosong], puzzle[kosong-1] = puzzle[kosong-1], puzzle[kosong]
  elif arah == 'd' and kol < 2:
    puzzle[kosong], puzzle[kosong+1] = puzzle[kosong+1], puzzle[kosong]
  else:
    print("Geseran tidak valid!")

def main():
  puzzle = buat_puzzle()
  tampilkan_puzzle(puzzle)

  while True:
    arah = input("Masukkan arah (w, a, s, d): ")
    geser(puzzle, arah)
    tampilkan_puzzle(puzzle)

    if puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
      print("Selamat, kamu berhasil menyelesaikan puzzle!")
      break

if __name__ == "__main__":
  main()