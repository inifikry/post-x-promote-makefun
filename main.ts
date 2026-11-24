// post-x-promote-make-your-own-bounty-01 entry (Node 22, standard library only).
// The entry is the X post itself: one post quoting make.fun's
// make-your-own-bounty post (https://x.com/makefunai/status/2124915864336236646),
// a photo of its own attached, make.fun and the play code in its text.
// This program only copies POST.json from the repository root to /output,
// where the gate reads the post's address. The house reads the post's
// replies, reposts and quotes from X itself; nothing written here is scored.
//
// POST.json ships with a placeholder address, so the gate refuses it as it
// stands. Replace it with the real post address before submitting.
//
// Local run:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(outDir, { recursive: true });
try {
  copyFileSync(join(botDir, 'POST.json'), join(outDir, 'POST.json'));
  console.log('POST.json copied to', join(outDir, 'POST.json'));
} catch (err) {
  console.error('Could not copy POST.json:', (err as Error).message);
  process.exit(1);
}
