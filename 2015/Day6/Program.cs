using System;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

namespace Day6
{
    class Program
    {
        static void Main(string[] args)
        {
            const Int32 BufferSize = 128;
            using (var fileStream = File.OpenRead("data.txt")) {
                using (var streamReader = new StreamReader(fileStream, Encoding.UTF8, true, BufferSize)) {
                    String line;
                    int[,] arr = new int[1000,1000];
                    while ((line = streamReader.ReadLine()) != null) {
                       char[] delims = {' ', ','};
                       String[] words = line.Split(delims);
                       if(words[0].Equals("turn")) {
                            int x1 = Int32.Parse(words[2]);
                            int y1 = Int32.Parse(words[3]);
                            int x2 = Int32.Parse(words[5]);
                            int y2 = Int32.Parse(words[6]);
                            for(int i = Math.Min(x1, x2); i <= Math.Max(x1, x2); i++) {
                                for(int j = Math.Min(y1, y2); j <= Math.Max(y1, y2); j++) {
                                    arr[i,j] += (words[1].Equals("on") ? 1 : (arr[i,j] == 0 ? 0 : -1));
                                }
                            }
                       } else {
                            int x1 = Int32.Parse(words[1]);
                            int y1 = Int32.Parse(words[2]);
                            int x2 = Int32.Parse(words[4]);
                            int y2 = Int32.Parse(words[5]);
                            for(int i = Math.Min(x1, x2); i <= Math.Max(x1, x2); i++) {
                                for(int j = Math.Min(y1, y2); j <= Math.Max(y1, y2); j++) {
                                    arr[i,j] += 2;
                                }
                            }
                       }
                    }
                    int c = 0;
                    for(int i = 0; i < 1000; i++) {
                        for(int j = 0; j < 1000; j++) {
                                c+=arr[i,j];
                        }
                    }
                    Console.WriteLine(c);
                }
            }
        }
    }
}
