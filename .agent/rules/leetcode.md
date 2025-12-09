---
trigger: always_on
description: LeetCode practice workspace - conventions, context và workflow cho assistant
---

# 🎮 LeetCode Practice Workspace

## 👤 Về User
- Người chơi game lâu năm, có nhiều kỹ năng trong hầu hết các game (không phải "game thủ" nhé!)
- Thích hệ thống gamification: XP, achievements, streaks, ranks
- Ngôn ngữ giao tiếp: Tiếng Việt

## 📁 Cấu trúc thư mục

```
leetcode/
├── problems/                    # Tất cả solutions
│   ├── 0001_two_sum.py
│   ├── 0014_longest_common_prefix.py
│   └── {số_bài_4_chữ_số}_{tên_bài}.py
├── daily_log.md                 # (Deprecated) - Dùng PROGRESS.md thay thế
├── PROGRESS.md                  # 🎮 Game-style progress tracker
└── .agent/workflows/            # Workflows và context
```

---

## 🎮 Hệ thống Gamification (PROGRESS.md)

### XP System
- Easy = 10 XP
- Medium = 25 XP
- Hard = 50 XP
- Daily Streak Bonus = +5 XP

### Rank System
| Rank | XP Required |
|------|-------------|
| 🥉 Bronze | 0 |
| 🥈 Silver | 100 |
| 🥇 Gold | 300 |
| 💎 Platinum | 600 |
| 👑 Diamond | 1000 |
| 🌟 Master | 2000 |

---

## � Workflow: Khi user đưa bài LeetCode MỚI

### 1. Tạo file solution template

Tạo file `problems/{số_4_chữ_số}_{tên_bài_snake_case}.py` với nội dung:

```python
"""
================================================================================
LeetCode #{số}: {Tên bài}
================================================================================
Difficulty: Easy/Medium/Hard
Date Started: YYYY-MM-DD
Link: https://leetcode.com/problems/{slug}/

--------------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------------
{Mô tả bài toán bằng tiếng Việt}

--------------------------------------------------------------------------------
Examples:
--------------------------------------------------------------------------------
{Copy examples từ đề bài}

--------------------------------------------------------------------------------
💡 Hints (Gợi ý):
--------------------------------------------------------------------------------
1. {Gợi ý 1 - nhẹ nhàng}
2. {Gợi ý 2 - cụ thể hơn}
3. {Gợi ý approach - nếu cần}

--------------------------------------------------------------------------------
🎯 Approach gợi ý: {Tên approach}
--------------------------------------------------------------------------------
{Giải thích ngắn gọn approach, KHÔNG code}

⏰ Time Complexity mục tiêu: O(...)
💾 Space Complexity mục tiêu: O(...)
"""

class Solution(object):
    def functionName(self, ...):
        """
        :type param: Type
        :rtype: ReturnType
        """
        # TODO: Implement your solution here
        pass


if __name__ == "__main__":
    sol = Solution()
    # Test cases - uncomment khi đã implement
    # print(sol.functionName(...))  # Expected: ...
```

### 2. KHÔNG làm những việc sau:
- ❌ Không code solution
- ❌ Không cập nhật PROGRESS.md (chờ user hoàn thành)
- ❌ Không spoil quá nhiều về cách giải

---

## ✅ Workflow: Khi user làm XONG 1 bài

1. **Cập nhật file solution** - thêm approach vào header nếu cần
2. **Cập nhật PROGRESS.md**:
   - Tăng Total Solved
   - Cập nhật streak
   - Thêm XP
   - Check achievements mới
   - Thêm entry vào Daily Quest Log

---

## 🔍 Workflow: Khi user yêu cầu REVIEW code

1. Phân tích code hiện tại
2. Chạy test cases để verify
3. Đánh giá:
   - Correctness
   - Time Complexity
   - Space Complexity
   - Readability
4. Đề xuất improvements nếu có
5. Giải thích các approach khác (nếu cần)
6. Cập nhật PROGRESS.md sau khi user hoàn thành

---

## 💡 Style Guide

- Comment bằng tiếng Việt khi giải thích logic phức tạp
- Sử dụng emoji trong PROGRESS.md để gamification
- Luôn include test cases trong `if __name__ == "__main__"`
- Đặt tên biến rõ ràng, có ý nghĩa

---

## 🚀 Workflow: Khi user yêu cầu CẢI TIẾN code

Khi user nói "cải tiến", "optimize", "tối ưu", "v2", etc:

### Điều kiện:
- ✅ Chỉ thêm v2 khi code của user **CHƯA tối ưu nhất**
- ❌ Nếu đã tối ưu → thông báo "Code đã tối ưu rồi!" và giải thích tại sao

### Nếu cần cải tiến:
1. **KHÔNG sửa code gốc** của user
2. **Thêm hàm mới** với suffix `_v2` hoặc `_enhanced`:
   ```python
   def searchInsert(self, nums, target):
       # Code gốc của user - giữ nguyên
       ...
   
   def searchInsert_v2(self, nums, target):
       # Phiên bản tối ưu hơn
       ...
       