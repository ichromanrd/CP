def solution(num):
    length = len(num)
    
    # flag the number sequence is correct
    is_valid = True

    # last left and right operand (after index 0 and 1)
    last_left_op = 0
    last_right_op = 0

    # flag whether skip current visited index
    should_skip_next = False
    # reserved next value of current element multiply by 10 and added by next index's element
    res_next = 0

    for i in range(length):
        if should_skip_next:
            # current index skipped but next will be visited again
            should_skip_next = False
            continue

        current = int(num[i])

        # if reserved value exists, use the reserved value instead. if not, stick to the current index's element
        if res_next > 0:
            current = res_next

        # skipping index 0 as it's already defined by default
        if i == 0:
            continue

        # verify index 1; skipping index 1 as it's just a result of 0 + index 0, if not then it's definitely invalid sequence
        if i == 1:
            if (0 + int(num[0])) == current:
                continue
            else:
                is_valid = False
                break

        # only verify the process if it's not index 0 and 1, and still in range of the list length
        if i > 1 and i < length:
            b1 = int(num[i - 1]) # means previous element - right operand
            b2 = int(num[i - 2]) # means element before previous - left operand

            # if last left and right operands recorded, use them instead of previous x-1 and x-2 elements, where x is current index
            if last_left_op > 0 and last_right_op > 0:
                b1 = last_right_op
                b2 = last_left_op

            # calculate next-supposed-to-be element (e.g left 7 right 7 then next must be 14)
            total_b = b1 + b2

            # if current element (which can be reserved next value) is still less than next-supposed-to-be element
            # then,
            if current < total_b:
                # validate if next index already out of range while current element still less than it supposed to be, then it's definitely invalid sequence
                if (i + 1) >= length:
                    is_valid = False    
                    break

                # calculate next element summed by current element multiplied by 10
                # let's say current is 1 and next element is 4, when they both are summed it should be 10 + 4 not 1 + 4
                # meaning 1 has to be multiplied by 10
                current_p_next = current * 10 + int(num[i + 1])

                # validate if the calculated next element matches the supposed-to-be next element then it's a valid sequence so far, continuing to the end of the sequence
                if current_p_next == total_b:
                    # since calculated next element already matches, next element won't be necessary to be visited, hence skipped
                    should_skip_next = True
                    # preserve last left operand as b1
                    last_left_op = b1
                    # preserve last right operand as calculated next element
                    last_right_op = current_p_next
                    # reset the reserved next value
                    res_next = 0
                    continue
                # but if calculated next element is still less than supposed-to-be next element then preserve the next element as current calculated element
                # e.g: left operand is 56, right operand 91, calculated next element must be 147
                # after visiting index with 1 value and add with its next element, it would be 14 but still less than 147
                # in this case preserve next element as 14 not 4, in which 14 will be multiplied by 10, making it 140 + next element 7, matches the sum of 56 + 91
                elif current_p_next < total_b:
                    res_next = current_p_next
                    continue
                # exhaustive check; if some sub-sequence elements already summed but it turns out bigger than the next supposed-to-be element
                # then it's definitely invalid sequence
                else:
                    is_valid = False
                    break
        
    print(f"{num} valid = {is_valid}")

solution('66121830')
solution('5510152540')
solution('11261')
solution('771421355691147')
solution('7714213556911472383856231008')
solution('771421355691147238385623100823')
solution('7714213556911472383856231008238812612')