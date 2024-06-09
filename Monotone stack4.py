class Solution:
    def trap(self, height: List[int]) -> int:
        area=0
        stack=[0]
        for i in range(1,len(height)):
            while stack and height[i]>height[stack[-1]]:
                mid=stack.pop()
                if not stack:
                    break
                left=height[stack[-1]]
                right=height[i]
                h=min(left,right)-height[mid]
                width=i-stack[-1]-1
                area+=(h*width)
            stack.append(i)
        return area
