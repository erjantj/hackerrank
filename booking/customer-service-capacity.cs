/*
HackerRank Customer Service Capacity
 
Problem: Determine how many people need to hire
  
Input specs:
- first line contains the current number of customer
  service executives
- second line contains a number of records in data set
- next linkes contains a pair of timestamps representing
  a start of call and end of call
  
Input demo:     
1
3
1481222000 1481222020
1481222000 1481222040
1481222030 1481222035
 
Output demo:
Expected result (number of additional customer service
executives):           
1
*/
using System;
using System.Collections.Generic;
 
namespace CustomerServiceCapacitySandbox
{
    class Solution
    {
        // HackeRank Solution
        static int numberOfAgentsToAdd(int numberOfAgents, int[][] callsTimes)
        {
            var set = new SortedList<int, int>();
            for (int i = 0; i < callsTimes.Length; ++i)
            {
                var b = callsTimes[i][0];
                var e = callsTimes[i][1];
 
                if (!set.ContainsKey(b)) set.Add(b, +1); else set[b]++;
                if (!set.ContainsKey(e)) set.Add(e, -1); else set[e]--;
            }
            var max = 0;
            var num = 0;
            foreach (var val in set.Values)
            {
                num += val;
                if (max < num) max = num;
            }
            return max - numberOfAgents;
        }
 
        static int Test00()
        {
            var numOfAgent = 1;
            var callsTimes = new int[3][];
 
            callsTimes[0] = new int[2];
            callsTimes[0][0] = 1481222000;
            callsTimes[0][1] = 1481222020;
            callsTimes[1] = new int[2];
            callsTimes[1][0] = 1481222000;
            callsTimes[1][1] = 1481222040;
            callsTimes[2] = new int[2];
            callsTimes[2][0] = 1481222030;
            callsTimes[2][1] = 1481222035;
 
            return numberOfAgentsToAdd(numOfAgent, callsTimes);
        }
 
        static int Test01()
        {
            var numOfAgent = 1;
            var callsTimes = new int[3][];
 
            callsTimes[0] = new int[2];
            callsTimes[0][0] = 1481222000;
            callsTimes[0][1] = 1481222020;
            callsTimes[1] = new int[2];
            callsTimes[1][0] = 1481222001;
            callsTimes[1][1] = 1481222040;
            callsTimes[2] = new int[2];
            callsTimes[2][0] = 1481222002;
            callsTimes[2][1] = 1481222035;
 
            return numberOfAgentsToAdd(numOfAgent, callsTimes);
        }
 
        static int Test02()
        {
            var numOfAgent = 1;
            var callsTimes = new int[3][];
 
            callsTimes[0] = new int[2];
            callsTimes[0][0] = 1481222000;
            callsTimes[0][1] = 1481222010;
            callsTimes[1] = new int[2];
            callsTimes[1][0] = 1481222020;
            callsTimes[1][1] = 1481222030;
            callsTimes[2] = new int[2];
            callsTimes[2][0] = 1481222040;
            callsTimes[2][1] = 1481222050;
 
            return numberOfAgentsToAdd(numOfAgent, callsTimes);
        }
 
        static int Test03()
        {
            var numOfAgent = 1;
            var callsTimes = new int[3][];
 
            callsTimes[0] = new int[2];
            callsTimes[0][0] = 1481222000;
            callsTimes[0][1] = 1481222050;
            callsTimes[1] = new int[2];
            callsTimes[1][0] = 1481222020;
            callsTimes[1][1] = 1481222050;
            callsTimes[2] = new int[2];
            callsTimes[2][0] = 1481222040;
            callsTimes[2][1] = 1481222050;
 
            return numberOfAgentsToAdd(numOfAgent, callsTimes);
        }
 
        static int Test04()
        {
            var numOfAgent = 1;
            var callsTimes = new int[4][];
 
            callsTimes[0] = new int[2];
            callsTimes[0][0] = 1481222000;
            callsTimes[0][1] = 1481222050;
            callsTimes[1] = new int[2];
            callsTimes[1][0] = 1481222020;
            callsTimes[1][1] = 1481222050;
            callsTimes[2] = new int[2];
            callsTimes[2][0] = 1481222040;
            callsTimes[2][1] = 1481222050;
            callsTimes[3] = new int[2];
            callsTimes[3][0] = 1481222050;
            callsTimes[3][1] = 1481222060;
 
            return numberOfAgentsToAdd(numOfAgent, callsTimes);
        }
 
        static int Test05()
        {
            var numOfAgent = 1;
            var callsTimes = new int[4][];
 
            callsTimes[0] = new int[2];
            callsTimes[0][0] = 1481222000;
            callsTimes[0][1] = 1481222050;
            callsTimes[1] = new int[2];
            callsTimes[1][0] = 1481222020;
            callsTimes[1][1] = 1481222050;
            callsTimes[2] = new int[2];
            callsTimes[2][0] = 1481222040;
            callsTimes[2][1] = 1481222050;
            callsTimes[3] = new int[2];
            callsTimes[3][0] = 1481222045;
            callsTimes[3][1] = 1481222060;
 
            return numberOfAgentsToAdd(numOfAgent, callsTimes);
        }
 
        static void TestRunner(Func<int> test, int expected)
        {
            int val = 0;
            Console.WriteLine(
              test.Method.Name + " = {0} -> {1}",
              (val = test.Invoke()), val == expected ? "PASS" : "FAIL");
        }
 
        static void Main(string[] args)
        {
            TestRunner(Test00, 1);
            TestRunner(Test01, 2);
            TestRunner(Test02, 0);
            TestRunner(Test03, 2);
            TestRunner(Test04, 2);
            TestRunner(Test05, 3);
 
            Console.WriteLine("Press any key to continue...");
 
            Console.ReadKey();
        }
    }
}
