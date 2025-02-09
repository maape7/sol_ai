// under testing

import { Connection, Commitment, PublicKey, TransactionSignature } from "@solana/web3.js";

async function fetchTransaction(txSignature: string): Promise<void> {
    // Initialize RPC client
    const rpcUrl = "https://api.devnet.solana.com";
    const commitment: Commitment = "confirmed";
    const connection = new Connection(rpcUrl, commitment);

    try {
        // Convert string to TransactionSignature (base58-encoded string)
        const signature: TransactionSignature = txSignature;

        // Fetch transaction details
        const tx = await connection.getTransaction(signature, {
            commitment: "confirmed",
            // encoding: "json",
        });

        if (!tx) {
            console.error("Transaction not found");
            return;
        }

        // Extract sender and receiver (first and second accounts)
        const accountKeys = tx.transaction.message.accountKeys;
        const sender: PublicKey = new PublicKey(accountKeys[0]);
        const receiver: PublicKey = new PublicKey(accountKeys[1]);

        console.log("Transaction Details:");
        console.log("- Blocktime:", tx.blockTime);
        console.log("- Transaction:", tx.transaction);

        // Please add it later, data type and access knowledge problem
        console.log("- Sender:", sender.toBase58());
        console.log("- Receiver:", receiver.toBase58());
    } catch (error) {
        console.error("Error fetching transaction:", error);
    }
}

// Example usage
// Input: Transaction Signature (e.g., 5VERv8...kQUW)
// → Output: Sender, Receiver, Blocktime
