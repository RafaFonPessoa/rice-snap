#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 -m venv "$SCRIPT_DIR/venv"
"$SCRIPT_DIR/venv/bin/pip" install pillow

cat <<EOF | sudo tee /usr/local/bin/rice-snap >/dev/null
#!/bin/bash
"$SCRIPT_DIR/venv/bin/python" "$SCRIPT_DIR/cli.py" "\$@"
EOF

sudo chmod +x /usr/local/bin/rice-snap
echo "rice-snap installed! Try: rice-snap ~/your-screenshot.png"
