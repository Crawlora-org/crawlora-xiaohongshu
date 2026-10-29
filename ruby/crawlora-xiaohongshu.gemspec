require_relative "lib/crawlora/xiaohongshu/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-xiaohongshu"
  spec.version = Crawlora::Xiaohongshu::VERSION
  spec.summary = "Xiaohongshu API client for Crawlora (4 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Xiaohongshu API. Covers public explore feeds, note details, comments, and search suggestions across 4 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=xiaohongshu-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-xiaohongshu", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-xiaohongshu/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
