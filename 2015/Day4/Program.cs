using System;
using System.Security.Cryptography;
using System.Text;


namespace C_
{
    class Program
    {
       static void Main() {
            int guess = 0;
            int finalGuess = 0;
            while(true) {
                string guessing = "iwrupvqb" + guess;
                string guessed = CalculateMD5(guessing);
                if(guessed.Length < 6) {
                    continue;
                }
                if(guessed.Substring(0, 6).Equals("000000")) {
                    finalGuess = guess;
                    break;
                }
                guess++;
            }
            Console.WriteLine("FINAL GUESS " + guess);
        }

         static string CalculateMD5(string input) {
            byte[] encodedPassword = new UTF8Encoding().GetBytes(input);
            byte[] hash = ((HashAlgorithm) CryptoConfig.CreateFromName("MD5")).ComputeHash(encodedPassword);
            string encoded = BitConverter.ToString(hash).Replace("-", string.Empty).ToLower();
            // Console.WriteLine(encoded);
            return encoded;
        }
    }
}
