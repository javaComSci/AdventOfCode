using System;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

namespace Day5
{
    class Program
    {
        static void Main(string[] args)
        {
            const Int32 BufferSize = 128;
            int countNice = 0;
            using (var fileStream = File.OpenRead("data.txt")) {
                using (var streamReader = new StreamReader(fileStream, Encoding.UTF8, true, BufferSize)) {
                    String line;
                    while ((line = streamReader.ReadLine()) != null) {
                        // bool vowelChecked = checkVowel(line);
                        // bool doubleLetter = checkDouble(line);
                        // bool goodString = checkStrings(line);

                        // if(vowelChecked && doubleLetter && goodString) {
                        //     countNice++;
                        // }

                        bool pairIn = pairInString(line);
                        bool middle = checkMiddle(line);

                        if(pairIn && middle) {
                            countNice ++;
                        }
                    }
                }
            }
            Console.WriteLine(countNice);
        }

        static bool pairInString(string s) {
            var map = new Dictionary<Tuple<char, char>, int>();
            for(int i = 0; i < s.Length - 1; i++) {
                Tuple<char, char> t = new Tuple<char, char>(s[i], s[i+1]);
                int value;
                if(map.TryGetValue(t, out value)) {
                    // check if it is not overlapping
                    if(value + 2 <= i) {
                        return true;
                    }
                } else {
                    map[t] = i;
                }  
            }
            return false;
        }

        static bool checkMiddle(string s) {
            for(int i = 0; i < s.Length - 2; i++) {
                if(s[i] == s[i+2]) {
                    return true;
                }
            }
            return false;
        }

        static bool checkVowel(string s) {
            int numVowels = 0;
            var vowels = new List<char> {'a','e','i','o','u'};
            for(int i = 0; i < s.Length; i++) {
                if(vowels.Contains(s[i])) {
                    numVowels += 1;
                }
            }

            if(numVowels >= 3) {
                return true;
            }
            return false;
        }

        static bool checkDouble(string s) {
            for(int i = 0; i < s.Length - 1; i++) {
                if(s[i] == s[i+1]) {
                    return true;
                }
            }
            return false;
        }

         static bool checkStrings(string s) {
            for(int i = 0; i < s.Length - 1; i++) {
                if((s[i] == 'a' && s[i+1] == 'b') || (s[i] == 'c' && s[i+1] == 'd') || (s[i] == 'p' && s[i+1] == 'q') || (s[i] == 'x' && s[i+1] == 'y')) {
                    return false;
                }
            }
            return true;
        }
    }
}
