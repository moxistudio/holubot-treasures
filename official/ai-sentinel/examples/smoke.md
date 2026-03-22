# Smoke Test

```bash
treasure-furnace preview https://github.com/moxistudio/holubot-treasures/tree/main/official/ai-sentinel
treasure-furnace install https://github.com/moxistudio/holubot-treasures/tree/main/official/ai-sentinel --runtime-assets-dir /tmp/ai-sentinel-preview
```

After preview or install, validate a minimal signal collection and briefing cycle with your local HoluBot runtime. Since the knowledge base isn't bundled yet, replace the KB reference with your team-managed knowledge repo or reference data when reviewing the results.
