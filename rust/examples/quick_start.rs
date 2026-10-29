use crawlora_xiaohongshu::{Client, ModelXiaohongshuExploreResponseDoc, XiaohongshuExploreParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .xiaohongshu
        .explore(XiaohongshuExploreParams {
            ..Default::default()
        })
        .await?;
    let data: ModelXiaohongshuExploreResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
