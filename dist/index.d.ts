export interface Icon {
  /** Base name with style and size stripped, e.g. "heart". */
  name: string;
  /** Full normalised name, e.g. "heart-outline-24". */
  slug: string;
  /** Original Meta filename. */
  file: string;
  /** Repository-relative path. */
  path: string;
  platform: "instagram" | "threads";
  variant: "web" | "ios" | "vector";
  format: "svg" | "png";
  style?: "outline" | "filled";
  /** Nominal size in points. */
  size?: number;
  viewBox?: string;
}

export interface Query {
  name?: string;
  slug?: string;
  style?: Icon["style"];
  size?: number;
  platform?: Icon["platform"];
  variant?: Icon["variant"];
  format?: Icon["format"];
}

export declare const icons: Icon[];
export declare const cdn: string;
export declare function filter(query?: Query): Icon[];
export declare function find(name: string, options?: Query): Icon | undefined;
export declare function url(icon: string | Icon): string | undefined;
export declare function sprite(icon: string | Icon): string | undefined;
