# App Bridge Free local smoke (list windows / read text / screenshot).
$ErrorActionPreference = "Stop"
$PluginRoot = Split-Path -Parent $PSScriptRoot
$Uv = if (Test-Path "$env:USERPROFILE\.local\bin\uv.exe") {
  "$env:USERPROFILE\.local\bin\uv.exe"
} else {
  "uv"
}
$McpSrc = Join-Path $PluginRoot "_windows_mcp_src"
if (-not (Test-Path (Join-Path $McpSrc "pyproject.toml"))) {
  Write-Error "Missing _windows_mcp_src. Clone https://github.com/1019666077-bit/Windows-MCP into that folder."
}

$env:WINDOWS_MCP_DISABLE_FLASH = "1"
Set-Location $McpSrc
& $Uv sync
& $Uv run python (Join-Path $PluginRoot "scripts\smoke_free.py")

# Verify MCP Free tool whitelist via CLI help / serve dry listing if available
$help = & $Uv run windows-mcp serve --help 2>&1 | Out-String
if ($help -notmatch "--tools") {
  Write-Warning "windows-mcp serve --help did not mention --tools"
}

Write-Host "SMOKE_OK plugin=$PluginRoot"
