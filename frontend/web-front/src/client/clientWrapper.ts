import {
    DefaultApi,
} from "./api";
import { Configuration } from "./configuration";

// dev環境
const basePath = "http://133.18.238.196/";

const option = {};

export const videoDataApi = new DefaultApi({baseOptions:option, basePath:basePath} as Configuration);