import Link from "next/link";
import type { Pet } from "@/lib/api";
import PetCard from "./PetCard";
import styles from "./PetTable.module.css";

interface Props {
  pets: Pet[];
}

export default function PetTable({ pets }: Props) {
  if (pets.length === 0) {
    return <p className={styles.empty}>No pets found.</p>;
  }

  return (
    <>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Name</th>
            <th>Species</th>
            <th>Gender</th>
            <th>Documents</th>
          </tr>
        </thead>
        <tbody>
          {pets.map((pet) => (
            <tr key={pet.id}>
              <td>
                <Link href={`/pets/${pet.id}`}>{pet.name}</Link>
              </td>
              <td className={styles.capitalize}>{pet.species}</td>
              <td className={styles.capitalize}>{pet.gender}</td>
              <td>{pet.documents.length}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className={styles.cards}>
        {pets.map((pet) => (
          <PetCard key={pet.id} pet={pet} />
        ))}
      </div>
    </>
  );
}
