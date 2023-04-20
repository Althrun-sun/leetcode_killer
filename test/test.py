import requests
from bs4 import BeautifulSoup


def get_problem_url(title_slug, difficulty):
    base_url = "https://leetcode.com"
    problems_url = f"{base_url}/api/problems/all/"

    response = requests.get(problems_url)
    if response.status_code == 200:
        problems = response.json()

        for problem in problems['stat_status_pairs']:
            if problem['stat']['question__title_slug'] == title_slug and problem['difficulty']['level'] == difficulty:
                problem_id = problem['stat']['question_id']
                return f"https://leetcode.com/problems/{title_slug}/"

    return None


# 示例：获取 "two-sum" 题目的 URL，难度为 1（简单）
url = get_problem_url("two-sum", 1)
print(url)
raw_data = {
    "Array_HashMap": [
        "Contains Duplicate",
        "Valid Anagram",
        "Concatenation of Array",
        "Replace Elements With Greatest Element On Right Side",
        "Is Subsequence",
        "Length of Last Word",
        "Two Sum",
        "Longest Common Prefix",
        "Group Anagrams",
        "Pascals Triangle",
        "Remove Element",
        "Unique Email Addresses",
        "Isomorphic Strings",
        "Can Place Flowers",
        "Majority Element",
        "Next Greater Element I",
        "Find Pivot Index",
        "Range Sum Query - Immutable",
        "Find All Numbers Disappeared in An Array",
        "Maximum Number of Balloons",
        "Word Pattern",
        "Design HashMap",
        "Sort an Array",
        "Top K Frequent Elements",
        "Product of Array Except Self",
        "Valid Sudoku",
        "Encode and Decode Strings",
        "Longest Consecutive Sequence",
        "Sort Colors",
        "Encode and Decode TinyURL",
        "Brick Wall",
        "Best Time to Buy And Sell Stock II",
        "Subarray Sum Equals K",
        "Unique Length 3 Palindromic Subsequences",
        "Minimum Number of Swaps to Make The String Balanced",
        "Number of Pairs of Interchangeable Rectangles",
        "Maximum Product of The Length of Two Palindromic Subsequences",
        "Grid Game",
        "Find All Anagrams in a String",
        "Find The Index of The First Occurrence in a String",
        "Wiggle Sort",
        "Largest Number",
        "Continuous Subarray Sum",
        "Push Dominoes",
        "Repeated DNA Sequences",
        "Insert Delete Get Random O(1)",
        "Check if a String Contains all Binary Codes of Size K",
        "Range Sum Query 2D Immutable",
        "Non Decreasing Array",
        "First Missing Positive"
    ],
    "Two_Pointers": [
        "Valid Palindrome",
        "Valid Palindrome II",
        "Minimum Difference Between Highest And Lowest of K Scores",
        "Reverse String",
        "Merge Sorted Array",
        "Move Zeroes",
        "Remove Duplicates From Sorted Array",
        "Remove Duplicates From Sorted Array II",
        "Two Sum II Input Array Is Sorted",
        "3Sum",
        "4Sum",
        "Container With Most Water",
        "Number of Subsequences That Satisfy The Given Sum Condition",
        "Rotate Array",
        "Array With Elements Not Equal to Average of Neighbors",
        "Boats to Save People",
        "Trapping Rain Water"
    ],
    "Sliding_window": [
        "Best Time to Buy And Sell Stock",
        "Contains Duplicate II",
        "Number of Sub Arrays of Size K and Avg Greater than or Equal to Threshold",
        "Longest Substring Without Repeating Characters",
        "Longest Repeating Character Replacement",
        "Permutation In String",
        "Frequency of The Most Frequent Element",
        "Minimum Number of Flips to Make The Binary String Alternating",
        "Minimum Size Subarray Sum",
        "Find K Closest Elements",
        "Minimum Window Substring",
        "Sliding Window Maximum"
    ],
    "Stack": [
        "Valid Parentheses",
        "Baseball Game",
        "Implement Stack Using Queues",
        "Min Stack",
        "Evaluate Reverse Polish Notation",
        "Generate Parentheses",
        "Asteroid Collision", "Daily Temperatures",
        "Online Stock Span",
        "Car Fleet",
        "Simplify Path",
        "Decode String",
        "Remove K Digits",
        "Remove All Adjacent Duplicates In String II",
        "132 Pattern",
        "Maximum Frequency Stack",
        "Largest Rectangle In Histogram"
    ],
    "Binary_Search": [
        "Binary Search",
        "Search Insert Position",
        "Guess Number Higher Or Lower",
        "Arranging Coins",
        "Squares of a Sorted Array",
        "Valid Perfect Square",
        "Search a 2D Matrix",
        "Koko Eating Bananas",
        "Find Minimum In Rotated Sorted Array",
        "Search In Rotated Sorted Array",
        "Time Based Key Value Store",
        "Find First And Last Position of Element In Sorted Array",
        "Maximum Number of Removable Characters",
        "Populating Next Right Pointers In Each Node",
        "Search Suggestions System",
        "Split Array Largest Sum",
        "Median of Two Sorted Arrays"
    ],
    "Linked_list": [
        "Reverse Linked List",
        "Merge Two Sorted Lists",
        "Palindrome Linked List",
        "Remove Linked List Elements",
        "Remove Duplicates From Sorted List",
        "Middle of the Linked List",
        "Intersection of Two Linked Lists",
        "Reorder List",
        "Maximum Twin Sum Of A Linked List",
        "Remove Nth Node From End of List",
        "Copy List With Random Pointer",
        "Design Linked List",
        "Design Browser History",
        "Add Two Numbers",
        "Linked List Cycle",
        "Find The Duplicate Number",
        "Swap Nodes In Pairs",
        "Sort List",
        "Partition List",
        "Rotate List",
        "Reverse Linked List II",
        "Design Circular Queue",
        "Insertion Sort List",
        "LRU Cache",
        "Merge K Sorted Lists",
        "Reverse Nodes In K Group"
    ],
    "Trees": [
        "Binary Tree Inorder Traversal",
        "Binary Tree Preorder Traversal",
        "Binary Tree Postorder Traversal",
        "Invert Binary Tree",
        "Maximum Depth of Binary Tree",
        "Diameter of Binary Tree",
        "Balanced Binary Tree",
        "Same Tree",
        "Subtree of Another Tree",
        "Convert Sorted Array to Binary Search Tree",
        "Merge Two Binary Trees",
        "Path Sum",
        "Construct String From Binary Tree",
        "Lowest Common Ancestor of a Binary Search Tree",
        "Insert into a Binary Search Tree",
        "Delete Node in a BST",
        "Binary Tree Level Order Traversal",
        "Binary Tree Right Side View",
        "Count Good Nodes In Binary Tree",
        "Validate Binary Search Tree",
        "Kth Smallest Element In a Bst",
        "Construct Binary Tree From Preorder And Inorder Traversal",
        "Unique Binary Search Trees",
        "Sum Root to Leaf Numbers",
        "House Robber III",
        "Flip Equivalent Binary Trees",
        "Operations On Tree",
        "All Possible Full Binary Trees",
        "Find Bottom Left Tree Value",
        "Trim a Binary Search Tree",
        "Binary Search Tree Iterator",
        "Convert Bst to Greater Tree",
        "Binary Tree Maximum Path Sum",
        "Serialize And Deserialize Binary Tree"
    ],
    "Heap": [
        "Kth Largest Element In a Stream",
        "Last Stone Weight",
        "K Closest Points to Origin",
        "Kth Largest Element In An Array",
        "Task Scheduler",
        "Design Twitter",
        "Single Threaded Cpu",
        "Seat Reservation Manager",
        "Process Tasks Using Servers",
        "Find The Kth Largest Integer In The Array",
        "Reorganize String",
        "Longest Happy String",
        "Car Pooling",
        "Find Median From Data Stream",
        "Maximum Performance of a Team",
        "IPO"
    ],
    "Backtracking": [
        "Subsets",
        "Combination Sum",
        "Combinations",
        "Permutations",
        "Subsets II",
        "Combination Sum II",
        "Permutations II",
        "Word Search",
        "Palindrome Partitioning",
        "Restore IP Addresses",
        "Letter Combinations of a Phone Number",
        "Matchsticks to Square",
        "Splitting a String Into Descending Consecutive Values",
        "Find Unique Binary String",
        "Maximum Length of a Concatenated String With Unique Characters",
        "Partition to K Equal Sum Subsets",
        "N Queens",
        "N Queens I"
    ],
    "Graphs": [
        "Island Perimeter",
        "Verifying An Alien Dictionary",
        "Number of Islands",
        "Clone Graph",
        "Max Area of Island",
        "Count Sub Islands",
        "Pacific Atlantic Water Flow",
        "Surrounded Regions",
        "Reorder Routes to Make All Paths Lead to The City Zero",
        "Rotting Oranges",
        "Walls And Gates",
        "Snakes And Ladders",
        "Open The Lock",
        "Find Eventual Safe States",
        "Course Schedule",
        "Course Schedule II",
        "Course Schedule IV",
        "Check if Move Is Legal",
        "Shortest Bridge",
        "Shortest Path in Binary Matrix",
        "Redundant Connection",
        "Number of Connected Components In An Undirected Graph",
        "Graph Valid Tree",
        "Accounts Merge",
        "Minimum Number of Days to Eat N Oranges",
        "Word Ladder"
    ],
    "Advanced_Graph": [
        "Reconstruct Itinerary",
        "Min Cost to Connect All Points",
        "Network Delay Time",
        "Path with Maximum Probability",
        "Swim In Rising Water",
        "Alien Dictionary",
        "Cheapest Flights Within K Stops"
    ],
    "Greedy_Algorithm": [
        "Maximum Subarray",
        "Maximum Sum Circular Subarray",
        "Longest Turbulent Array",
        "Jump Game",
        "Jump Game II",
        "Jump Game VII",
        "Gas Station",
        "Hand of Straights",
        "Maximum Points You Can Obtain From Cards",
        "Merge Triplets to Form Target Triplet",
        "Partition Labels",
        "Valid Parenthesis String",
        "Eliminate Maximum Number of Monsters",
        "Two City Scheduling"
    ],
    "Intervals": [
        "Insert Interval",
        "Merge Intervals",
        "Non Overlapping Intervals",
        "Meeting Rooms",
        "Meeting Rooms II",
        "Remove Covered Intervals",
        "Minimum Interval to Include Each Query"
    ]
}

category_counts = {category: len(problems) for category, problems in raw_data.items()}
print(category_counts)
import re

problem_details = {}
leetcode_url = "https://leetcode.com/problems/"

for category, problems in raw_data.items():
    problem_details[category] = []
    for problem in problems:
        # 将题目名称转换为URL格式
        problem_url = re.sub(r'\s+', '-', problem.lower())
        problem_url = re.sub(r"[^a-zA-Z0-9-]", "", problem_url)
        full_url = leetcode_url + problem_url
        
        # 添加题目详细信息到字典
        problem_details[category].append({
            "title": problem,
            "url": full_url,
            "difficulty": "unknown",
            "completed": False
        })

# 打印题目详细信息
print(problem_details)
