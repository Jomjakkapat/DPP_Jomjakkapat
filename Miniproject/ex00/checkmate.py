def is_in_check(*rows: str) -> bool | None:
    if not rows or any(not isinstance(row, str) for row in rows):
        return None

    size = len(rows)
    if size != len(rows[0]) or any(len(row) != size for row in rows):
        return None

    kings = [
        (row_index, column_index)
        for row_index, row in enumerate(rows)
        for column_index, square in enumerate(row)
        if square == "K"
    ]
    if len(kings) != 1:
        return None

    king_row, king_column = kings[0]
    in_check = False

    for row_step in (-1, 0, 1):
        for column_step in (-1, 0, 1):
            if row_step == 0 and column_step == 0:
                continue

            row = king_row + row_step
            column = king_column + column_step
            while 0 <= row < size and 0 <= column < size:
                piece = rows[row][column]
                if piece in "BQR":
                    is_straight = row_step == 0 or column_step == 0 
                    if piece == "Q" or (piece == "R" and is_straight) or (
                        piece == "B" and not is_straight
                    ):
                        in_check = True
                    break
                if piece == "P":
                    break
                row += row_step
                column += column_step
            if in_check:
                break
        if in_check:
            break

    if not in_check and king_row < size - 1:
        for column_step in (-1, 1):
            pawn_column = king_column + column_step
            if (
                0 <= pawn_column < size
                and rows[king_row + 1][pawn_column] == "P"
            ):
                in_check = True
                break

    return in_check


def checkmate(*rows: str) -> None:
    in_check = is_in_check(*rows)
    if in_check is not None:
        print("Success" if in_check else "Fail")
