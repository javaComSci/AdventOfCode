using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

namespace Day7
{
    class Program
    {  
        static bool isNotWord(String s) {
            return !s.Equals("->");
        }
        static void Main(string[] args)
        {
            Dictionary<String,  uint> inputs = new Dictionary<String, uint>();
            List<String> linesLeft = new List<String>();
            const Int32 BufferSize = 128;
            using (var fileStream = File.OpenRead("data.txt")) {
                using (var streamReader = new StreamReader(fileStream, Encoding.UTF8, true, BufferSize)) {
                    String line;
                    while ((line = streamReader.ReadLine()) != null || linesLeft.Count != 0) {
                        string[] words;
                        Console.WriteLine(linesLeft.Count);
                        if(line != null) {
                            words = line.Split(' ');
                            words = Array.FindAll(words, isNotWord);
                        } else {
                            var a = linesLeft[0];
                            line = linesLeft[0];
                            words = a.Split(' ');
                            words = Array.FindAll(words, isNotWord);
                            linesLeft.RemoveAt(0);
                            Console.WriteLine("THE LINE IS " + line);
                        }
                        
                        
                        if(words[0].Equals("NOT")) {
                            if(inputs.ContainsKey(words[1])) {
                                inputs[words[2]] = ~inputs[words[1]];
                            } else {
                                linesLeft.Add(line);
                            }
                        } else if (words[1].Equals("AND")) {
                            if(inputs.ContainsKey(words[0]) && inputs.ContainsKey(words[2])) {
                                inputs[words[3]] = inputs[words[0]] & inputs[words[2]];
                            } else {
                                linesLeft.Add(line);
                            }
                        } else if (words[1].Equals("OR")) {
                            if(inputs.ContainsKey(words[0]) && inputs.ContainsKey(words[2])) {
                                inputs[words[3]] = inputs[words[0]] | inputs[words[2]];
                            } else {
                                linesLeft.Add(line);
                            }
                        } else if (words[1].Equals("LSHIFT")) {
                            if(inputs.ContainsKey(words[0])) {
                                inputs[words[3]] = inputs[words[0]] << Int32.Parse(words[2]);
                            } else {
                                linesLeft.Add(line);
                            }
                        } else if (words[1].Equals("RSHIFT")) {
                            if(inputs.ContainsKey(words[0])) {
                                inputs[words[3]] = inputs[words[0]] >> Int32.Parse(words[2]);
                            } else {
                                linesLeft.Add(line);
                            }
                        } else {
                            try {
                                inputs[words[1]] = (uint)Int32.Parse(words[0]);
                            } catch (Exception e) {
                                if(inputs.ContainsKey(words[0])) {
                                    inputs[words[1]] = inputs[words[0]];
                                } else {
                                    linesLeft.Add(line);
                                }
                            }
                            
                        }
                    }
                }
            }
            foreach (KeyValuePair<String, uint> kvp in inputs) {
                // if(kvp.Key.Equals("a")) {
                    Console.WriteLine("Key = {0}, Value = {1}", kvp.Key, (ushort) kvp.Value);
                // }
                
            }
        }
    }
}
