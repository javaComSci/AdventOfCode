using System;
using System.Security.Cryptography;
using System.Text;

namespace Day4 {
    class Day4 {
        static void Main() {
            int guess = 0;
            string finalGuess = "";
            while(true) {
                string guessing = "iwrupvqb" + guess;
                string guessed = CalculateMD5(guessing);
                if(guessed.Length < 5) {
                    continue;
                }
                if(guessed.Substring(0, 5).Equals("00000")) {
                    finalGuess = guessed;
                    break;
                }
                guess++;
            }
            return finalGuess;
            Console.WriteLine(finalGuess);
        }

        static string CalculateMD5(string input) {
            byte[] encodedPassword = new UTF8Encoding().GetBytes(input);
            byte[] hash = ((HashAlgorithm) CryptoConfig.CreateFromName("MD5")).ComputeHash(encodedPassword);
            string encoded = BitConverter.ToString(hash).Replace("-", string.Empty).ToLower();
            Console.WriteLine("LKSDFKLJSD");
            Console.WriteLine(input);
            return encoded;
        }
    }
}
