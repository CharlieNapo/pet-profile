export interface PetDocument {
  id: string;
  name: string;
  url: string;
  created_at: string;
}

export interface Pet {
  id: string;
  name: string;
  date_of_birth: string;
  species: "cat" | "dog";
  gender: "male" | "female";
  documents: PetDocument[];
  created_at: string;
  updated_at: string;
}

const BASE_URL = process.env.BACKEND_URL ?? "http://backend:8000";

export async function getPets(species?: string): Promise<Pet[]> {
  const url = new URL("/api/pets", BASE_URL);
  if (species) {
    url.searchParams.set("species", species);
  }
  const res = await fetch(url.toString(), { cache: "no-store" });
  if (!res.ok) {
    throw new Error(`Failed to fetch pets: ${res.status}`);
  }
  return res.json();
}

export async function getPetById(id: string): Promise<Pet | null> {
  const res = await fetch(`${BASE_URL}/api/pets/${id}`, { cache: "no-store" });
  if (res.status === 404) {
    return null;
  }
  if (!res.ok) {
    throw new Error(`Failed to fetch pet: ${res.status}`);
  }
  return res.json();
}
