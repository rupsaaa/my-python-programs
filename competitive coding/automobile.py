'''Problem Statement: An automobile company manufactures both two-wheelers (TW) and four-wheelers (FW). A company manager wants to make the production of both types of vehicles according to the given data below:
Total number of vehicles (two-wheeler + four-wheeler) = V
Total number of wheels = W
The task is to find how many two-wheelers and four-wheelers need to be manufactured as per the given data.
Example:Input:V = 200  W=540
Output:TW = 130 fW = 70
Explanation:130 + 70 = 200 vehicles
(70 * 4) + (130 * 2) = 540 wheels
Constraints:
2 <= W W % 2 = 0 V < W
Print "INVALID INPUT" if inputs do not meet the constraints.'''
v=int(input("Enter no.of vehicles:"))
w=int(input("Enter no.of wheels:"))
if w>=2 and w%2==0 and v<w:
    fw=(w//2)-v
    tw=v-fw
    print("TW=",tw)
    print("FW=",fw)
else:
    print("INVALID INPUT")
