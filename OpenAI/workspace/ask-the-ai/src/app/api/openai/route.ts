// src/app/api/openai/route.ts
 
import { NextRequest, NextResponse } from 'next/server';
import OpenAI from "openai";
 
const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
});
 
export async function POST(request: NextRequest) {
  if (request.method !== 'POST') {
    return NextResponse.json({ error: 'Method not allowed' }, { status: 405 });
  }
 
  try {
    const requestBody = await request.json();
    const { query } = requestBody;
 
    if (!query) {
      return NextResponse.json({ error: 'Query not provided' }, { status: 400 });
    }
 
    const chatCompletion = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [{ role: "user", content: query }]
    });
 
    if (!chatCompletion || !chatCompletion.choices || chatCompletion.choices.length === 0) {
      console.error('Invalid response from OpenAI:', chatCompletion);
      return NextResponse.json({ error: 'Invalid response from OpenAI' }, { status: 500 });
    }
 
    // Extract the AI response from the content property of the message object
    const aiResponse = chatCompletion.choices[0].message.content || 'No response content';
 
    return NextResponse.json({ response: aiResponse });
  } catch (error) {
    console.error('Error processing the request:', error);
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}