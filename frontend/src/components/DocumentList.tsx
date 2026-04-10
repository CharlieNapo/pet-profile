import type { PetDocument } from "@/lib/api";
import styles from "./DocumentList.module.css";

interface Props {
  documents: PetDocument[];
}

export default function DocumentList({ documents }: Props) {
  if (documents.length === 0) {
    return <p className={styles.empty}>No documents.</p>;
  }

  return (
    <ul className={styles.list}>
      {documents.map((doc) => (
        <li key={doc.id} className={styles.item}>
          <a href={doc.url} target="_blank" rel="noopener noreferrer">
            {doc.name}
          </a>
        </li>
      ))}
    </ul>
  );
}
