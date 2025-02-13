import axios from "axios";
import { Request, Response } from "express";
import { getNFTMetadata } from "../nft";


export const sendToFastAPI = async (req: Request, res: Response) => {
    try {

        
        // later keep 
        const { mintAddress } = req.body;


        console.log("mintAddress -->", mintAddress)

        // const mintAddress = "8qfPaiceC1xR7dfePdW74k7TP4sH9AG7nRrr9acSGZNg";
        // const data = await getNFTMetadata(mintAddress);

        const data = {

           "external_url":"https://www.solanamoneyboys.xyz",
           "description": "Get exclusive Solana tokens now—only a few left!"

        }

        
        const fastApiUrl = process.env.FASTAPI_URL || "http://localhost:8000/api/analyze";
        // Send data to FastAPI
        if (data) {
            const response = await axios.post(fastApiUrl, {
                nft_metadata: data.external_url, // Send all NFT metadata properly
                description: data.description // Ensure 'description' is properly accessed
            });
           
            console.log(" nft_metadata: data.external_url", data.external_url)
            console.log(" description: data.description ",  data.description )
            console.log("API Response:", response.data);
            res.status(201).json(response.data);
        }
       
    } catch (error) {
        console.error("Error processing fraud check:", error);
        res.status(500).json({ error: "Error processing fraud check" });
    }
};

// exampel
// Define the data to send
        // const nft_metadata = { external_url: "https://official-giveaway.xyz" };
        // const project_metrics = {
        //     transactions_last_30_days: 5,
        //     top_wallet_percentage: 60,
        //     secondary_sales_count: 0,
        // };
        // const description = "This is a guaranteed risk-free official giveaway! Act now.";



        // testing 
        // const data = {

        //    "external_url":"https://www.solanamoneyboys.com",
        //    "description": "building the metaverse"

        // }
