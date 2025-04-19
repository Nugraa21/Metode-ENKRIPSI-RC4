// RC4 Algorithm Implementation
function rc4(key, input) {
    const S = [];
    const keyLength = key.length;
  
    // Step 1: Key-Scheduling Algorithm (KSA)
    for (let i = 0; i < 256; i++) {
      S[i] = i;
    }
  
    let j = 0;
    for (let i = 0; i < 256; i++) {
      j = (j + S[i] + key.charCodeAt(i % keyLength)) % 256;
      [S[i], S[j]] = [S[j], S[i]]; // Swap
    }
  
    // Step 2: Pseudo-Random Generation Algorithm (PRGA)
    let i = 0;
    j = 0;
    const result = [];
    for (let char of input) {
      i = (i + 1) % 256;
      j = (j + S[i]) % 256;
      [S[i], S[j]] = [S[j], S[i]]; // Swap
      const k = S[(S[i] + S[j]) % 256];
      result.push(String.fromCharCode(char.charCodeAt(0) ^ k)); // XOR operation
    }
  
    return result.join('');
  }
  
  // DOM Manipulation
  document.getElementById('encrypt-btn').addEventListener('click', () => {
    const plaintext = document.getElementById('plaintext').value;
    const key = document.getElementById('key').value;
    if (!plaintext || !key) {
      alert('Please enter both plaintext and key!');
      return;
    }
  
    const ciphertext = rc4(key, plaintext);
    document.getElementById('output').value = btoa(ciphertext); // Encode as Base64
  });
  
  document.getElementById('decrypt-btn').addEventListener('click', () => {
    const ciphertext = document.getElementById('plaintext').value;
    const key = document.getElementById('key').value;
    if (!ciphertext || !key) {
      alert('Please enter both ciphertext and key!');
      return;
    }
  
    const decodedCiphertext = atob(ciphertext); // Decode Base64
    const plaintext = rc4(key, decodedCiphertext);
    document.getElementById('output').value = plaintext;
  });
  