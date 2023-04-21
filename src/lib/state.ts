import { writable } from 'svelte/store';
import type { Writable } from 'svelte/store';
import type { GameManager } from './game'

export const gameManagerStore: Writable<GameManager | undefined> = writable(undefined);
