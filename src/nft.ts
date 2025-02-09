import { Metaplex, keypairIdentity } from "@metaplex-foundation/js";
import { Connection, PublicKey } from "@solana/web3.js";

async function getNFTMetadata(mintAddress: string) {
  // Initialize the connection to the Solana cluster
  const connection = new Connection("https://api.mainnet-beta.solana.com", "confirmed");



  // Initialize Metaplex with the connection
  const metaplex = new Metaplex(connection);

  // Convert the mint address to a PublicKey
  const mint = new PublicKey(mintAddress);

  // Fetch the NFT metadata
  const nft = await metaplex.nfts().findByMint({ mintAddress: mint });


  // Log the NFT metadata
  console.log({
    name: nft.name,  // ✅ NFT project name (Correct)
    symbol: nft.symbol,  // ✅ Token symbol (Correct)
    description: nft.json?.description,  // ✅ NFT description (Correct)
    image: nft.json?.image,  // ✅ Image URL (Correct)
    external_url: nft.json?.external_url,  // ✅ Project's external URL (Correct)
    seller_fee_basis_points: nft.sellerFeeBasisPoints,  // ✅ Royalties percentage (Correct)
    creators: nft.creators?.map(creator => creator.address.toBase58()),  // ✅ Creator addresses (Correct)
    update_authority: nft.updateAuthorityAddress.toBase58(),  // ✅ Who controls updates? (Correct)
    mint_address: nft.address.toBase58(),  // ✅ Mint address (Fixed Error: nft.address instead of nft.mintAddress)
    metadata_uri: nft.uri,  // ✅ Metadata URI (Correct)
});

  return nft.json;
}

// Example mint address
const mintAddress = "8qfPaiceC1xR7dfePdW74k7TP4sH9AG7nRrr9acSGZNg";
getNFTMetadata(mintAddress);

// → Input: Mint Address (e.g., metaqbxx...518x1s)
// → Output:  name: nft.name,  // ✅ NFT project name (Correct)
    // symbol: nft.symbol,  // ✅ Token symbol (Correct)
    // description: nft.json?.description,  // ✅ NFT description (Correct)
    // image: nft.json?.image,  // ✅ Image URL (Correct)
    // external_url: nft.json?.external_url,  // ✅ Project's external URL (Correct)
    // seller_fee_basis_points: nft.sellerFeeBasisPoints,  // ✅ Royalties percentage (Correct)
    // creators: nft.creators?.map(creator => creator.address.toBase58()),  // ✅ Creator addresses (Correct)
    // update_authority: nft.updateAuthorityAddress.toBase58(),  // ✅ Who controls updates? (Correct)
    // mint_address: nft.address.toBase58(),  // ✅ Mint address (Fixed Error: nft.address instead of nft.mintAddress)
    // metadata_uri: nft.uri,  // ✅ Metadata URI (Correct)